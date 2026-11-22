import pytest

from groq_chat import MODEL, ask_groq


@pytest.fixture
def fake_client(mocker):
    choice = mocker.Mock()
    choice.message.content = "4"
    response = mocker.Mock()
    response.choices = [choice]
    client = mocker.Mock()
    client.chat.completions.create.return_value = response
    return client


def test_ask_groq(fake_client):
    assert ask_groq("What is 2+2?", client=fake_client) == "4"


def test_ask_groq_calls_api_correctly(fake_client):
    ask_groq("What is 2+2?", client=fake_client)
    fake_client.chat.completions.create.assert_called_once_with(
        model=MODEL,
        messages=[{"role": "user", "content": "What is 2+2?"}],
        max_tokens=1024,
    )


@pytest.mark.parametrize("question", ["", "   ", "\n"])
def test_empty_question_never_reaches_the_api(mocker, question):
    client = mocker.Mock()
    with pytest.raises(ValueError, match="cannot be empty"):
        ask_groq(question, client=client)
    client.chat.completions.create.assert_not_called()


@pytest.mark.slow
def test_marked_slow(fake_client):
    assert sum(range(100_000)) == 4_999_950_000
    assert ask_groq("q", client=fake_client) == "4"


@pytest.mark.fast
def test_marked_fast(fake_client):
    assert ask_groq("q", client=fake_client) == "4"
