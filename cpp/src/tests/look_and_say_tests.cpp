#include <look_and_say.hpp>

#include <gtest/gtest.h>


struct TestCase
{
    uint32_t sequence_number;
    uint64_t expected_length;
};

class LookAndSayTestFixture : public ::testing::TestWithParam<TestCase>
{
};

TEST_P(LookAndSayTestFixture, getLength_shouldReturnLength)
{
    ASSERT_EQ(look_and_say::getLengthOfSequence(GetParam().sequence_number), GetParam().expected_length);
}

INSTANTIATE_TEST_CASE_P(getLengthTests, LookAndSayTestFixture,
                        ::testing::Values(TestCase{0, 0}, TestCase{1, 1}, TestCase{2, 2}, TestCase{3, 2},
                                          TestCase{30, 4462}));

TEST(LookAndSayTest, getSequence)
{
    ASSERT_EQ(look_and_say::getSequence(15), "311311222113111231131112132112311321322112111312211312111322212311322113212221");
}
