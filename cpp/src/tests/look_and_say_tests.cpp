#include <common/look_and_say.hpp>
#include <cosmo/look_and_say.hpp>

#include <gtest/gtest.h>

namespace
{
struct TestCase
{
    uint32_t sequence_number;
    uint64_t expected_length;
};

class LookAndSayTestFixture : public ::testing::TestWithParam<TestCase>
{
};
} // namespace

TEST_P(LookAndSayTestFixture, common_getLength_shouldReturnLength)
{
    ASSERT_EQ(look_and_say::common::getLengthOfSequence(GetParam().sequence_number), GetParam().expected_length);
}
TEST_P(LookAndSayTestFixture, cosmo_getLength_shouldReturnLength)
{
    ASSERT_EQ(look_and_say::cosmo::getLengthOfSequence(GetParam().sequence_number), GetParam().expected_length);
}

INSTANTIATE_TEST_CASE_P(getLengthTests, LookAndSayTestFixture,
                        ::testing::Values(TestCase{0, 0}, TestCase{1, 1}, TestCase{2, 2}, TestCase{3, 2},
                                          TestCase{30, 4462}));

TEST(LookAndSayTest, getSequence)
{
    ASSERT_EQ(look_and_say::common::getSequence(15),
              "311311222113111231131112132112311321322112111312211312111322212311322113212221");
}

TEST(LookAndSayTest, output_of_different_implementations_is_equal)
{
    for (size_t i = 0; i <= 70; ++i)
        ASSERT_EQ(look_and_say::common::getSequence(i), look_and_say::cosmo::getSequence(i));
}
