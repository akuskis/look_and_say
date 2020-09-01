#include "look_and_say.hpp"

#include <vector>


namespace look_and_say::common
{
uint64_t getLengthOfSequence(uint32_t sequence_number)
{
    return getSequence(sequence_number).length();
}

std::string getSequence(uint32_t sequence_number)
{
    if (sequence_number == 0)
        return "";

    std::vector<uint8_t> sequence{1};

    while (--sequence_number > 0)
    {
        std::vector<uint8_t> temporary;

        uint8_t c = sequence[0];
        uint8_t count = 0;

        auto store = [&c, &count, &temporary]() {
          temporary.push_back(count);
          temporary.push_back(c);
        };

        for (size_t i = 0; i < sequence.size(); ++i, ++count)
        {
            if (c != sequence[i])
            {
                store();
                c = sequence[i];
                count = 0;
            }
        }

        store();
        std::swap(sequence, temporary);
    }

    std::string seq;
    for (auto const item : sequence)
        seq.append(std::to_string(item));

    return seq;
}
} // namespace look_and_say::common
