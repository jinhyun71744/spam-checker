import pytest
from spam import check_spam


def test_cheap_and_discount_marked_spam():
	result, hit = check_spam("This is a cheap discount offer")
	assert result == "spam"
	assert hit >= 2


def test_single_keyword_not_spam():
	result, hit = check_spam("This is a cheap")
	assert result == "ham"
	assert hit == 1

