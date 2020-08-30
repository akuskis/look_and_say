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

INSTANTIATE_TEST_CASE_P(LeapYearTests, LookAndSayTestFixture,
                        ::testing::Values(TestCase{1, 1}, TestCase{2, 2}, TestCase{3, 2}));
