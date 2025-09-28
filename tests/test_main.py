from camm_hackathon.main import main

def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert "Hello, world!" in captured.out
