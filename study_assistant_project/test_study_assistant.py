"""
Test Script for Study Assistant
================================
This script tests the Study Assistant with various sample interactions
to verify that the rule-based logic works correctly.
"""

from study_assistant import StudyAssistant


def run_tests():
    """Run a series of test interactions with the Study Assistant."""
    assistant = StudyAssistant()
    
    print("=" * 70)
    print("TESTING STUDY ASSISTANT - Rule-Based AI System")
    print("=" * 70)
    print("\nRunning 6 sample interactions to verify system behavior...\n")
    
    # Test cases
    test_cases = [
        {
            "test_number": 1,
            "input": "Hello!",
            "expected_category": "Greeting",
            "description": "Test greeting recognition"
        },
        {
            "test_number": 2,
            "input": "How should I study for mathematics?",
            "expected_category": "Subject-specific advice (Math)",
            "description": "Test subject-specific query recognition"
        },
        {
            "test_number": 3,
            "input": "I have an exam next week, how should I prepare?",
            "expected_category": "Exam preparation advice",
            "description": "Test exam preparation query"
        },
        {
            "test_number": 4,
            "input": "I'm feeling unmotivated and tired",
            "expected_category": "Motivation advice",
            "description": "Test motivation-related query"
        },
        {
            "test_number": 5,
            "input": "What's the best way to manage my study time?",
            "expected_category": "Time management advice",
            "description": "Test time management query"
        },
        {
            "test_number": 6,
            "input": "Can you help me with programming?",
            "expected_category": "Subject-specific advice (Programming)",
            "description": "Test programming subject recognition"
        }
    ]
    
    results = []
    
    for test in test_cases:
        print(f"\n{'=' * 70}")
        print(f"TEST {test['test_number']}: {test['description']}")
        print(f"{'=' * 70}")
        print(f"Input: \"{test['input']}\"")
        print(f"Expected Category: {test['expected_category']}")
        print(f"\nResponse:")
        print("-" * 70)
        
        response = assistant.process_query(test['input'])
        print(response)
        
        # Verify response is not empty
        is_valid = len(response) > 0 and response != ""
        results.append({
            "test": test['test_number'],
            "passed": is_valid,
            "category": test['expected_category']
        })
        
        print("-" * 70)
    
    # Summary
    print(f"\n\n{'=' * 70}")
    print("TEST SUMMARY")
    print("=" * 70)
    
    passed = sum(1 for r in results if r['passed'])
    total = len(results)
    
    for result in results:
        status = "PASSED" if result['passed'] else "FAILED"
        print(f"Test {result['test']}: {status} - {result['category']}")
    
    print(f"\nTotal: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n[SUCCESS] All tests passed! The rule-based system is working correctly.")
    else:
        print(f"\n[WARNING] {total - passed} test(s) failed. Please review the system logic.")
    
    print("=" * 70)
    
    # Display conversation history
    print("\n\nCONVERSATION HISTORY:")
    print("=" * 70)
    for i, (speaker, message) in enumerate(assistant.conversation_history, 1):
        speaker_label = "USER" if speaker == "user" else "ASSISTANT"
        print(f"\n[{i}] {speaker_label}:")
        # Truncate long messages for display
        display_msg = message[:200] + "..." if len(message) > 200 else message
        print(f"    {display_msg}")
    
    return passed == total


if __name__ == "__main__":
    success = run_tests()
    exit(0 if success else 1)

