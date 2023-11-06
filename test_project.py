from project import check_input_help, digits, printable, creaete_acc_db, Err_AccAlreadyExist, log_in_db, add, update, delete, show,  take_pass, check_exist
import os 
import pytest


def test_check_input_help():
    assert check_input_help(inpt="0", length_min=2) == True
    assert check_input_help(inpt="555", length_max=2) == True
    assert check_input_help(inpt="l.", ) == True
    assert check_input_help(inpt="yes", condition=printable) == False
    assert check_input_help(inpt="asdasda", condition=digits) == True
    assert check_input_help(inpt="4654", condition=digits) == False
    assert check_input_help(inpt=".x") == True
    with pytest.raises(EOFError):
        check_input_help(inpt=".quit")
        check_input_help(inpt=".exit")


def test_creaete_acc_db():
    if os.path.exists("pytest.db"):
        os.remove("pytest.db")
    assert creaete_acc_db("pytest.db", "test",) == True
    with pytest.raises(Err_AccAlreadyExist):
        creaete_acc_db("pytest.db", "test",)
    os.remove("pytest.db")


def test_log_in_db():
    if os.path.exists("pytest.db"):
        os.remove("pytest.db")
    creaete_acc_db("pytest.db", "test",)
    assert log_in_db("pytest.db", "test") == True
    with pytest.raises(Exception):
        log_in_db("pytest1.db", "test")
    os.remove("pytest.db")
    os.remove("pytest1.db")


def test_add_show():
    if os.path.exists("pytest.db"):
        os.remove("pytest.db")
    creaete_acc_db("pytest.db", "test",)
    assert add("pytest.db", "test", "test_app", "test_name", "test@mail.com", "test.com", "test_pass") == True
    assert show("pytest.db", "test", "test_app") == [('test_app', 'test_name', 'test@mail.com', 'test.com', 'test_pass')]
    with pytest.raises(Exception):
        add("pytest.db", "test", "test_app", "test_name", "test@mail.com", "test.com", "test_pass")
    os.remove("pytest.db")


def test_delete_show_add():
    if os.path.exists("pytest.db"):
        os.remove("pytest.db")
    creaete_acc_db("pytest.db", "test",)
    assert add("pytest.db", "test", "test_app", "test_name", "test@mail.com", "test.com", "test_pass") == True
    assert show("pytest.db", "test", "test_app") == [('test_app', 'test_name', 'test@mail.com', 'test.com', 'test_pass')]
    assert delete("pytest.db", "test", "test_app") == True
    with pytest.raises(Exception):
        show("pytest.db", "test", "test_app")
    os.remove("pytest.db")



def test_update_show_add():
    if os.path.exists("pytest.db"):
        os.remove("pytest.db")
    creaete_acc_db("pytest.db", "test",)
    assert add("pytest.db", "test", "test_app", "test_name", "test@mail.com", "test.com", "test_pass") == True
    assert show("pytest.db", "test", "test_app") == [('test_app', 'test_name', 'test@mail.com', 'test.com', 'test_pass')]
    assert update("pytest.db", "test", "test_app", "test_nameg", "test@mail.comg", "test.comg", "test_passg")
    assert show("pytest.db", "test", "test_app") == [('test_app', 'test_nameg', 'test@mail.comg', 'test.comg', 'test_passg')]
    os.remove("pytest.db")


def test_take_pass_show_add():
    if os.path.exists("pytest.db"):
        os.remove("pytest.db")
    creaete_acc_db("pytest.db", "test",)
    assert add("pytest.db", "test", "test_app", "test_name", "test@mail.com", "test.com", "test_pass") == True
    assert show("pytest.db", "test", "test_app") == [('test_app', 'test_name', 'test@mail.com', 'test.com', 'test_pass')]
    assert take_pass("pytest.db", "test", "test_app") == "test_pass"
    os.remove("pytest.db")


def test_check_exist():
    if os.path.exists("pytest.db"):
        os.remove("pytest.db")
    creaete_acc_db("pytest.db", "test",)
    assert add("pytest.db", "test", "test_app", "test_name", "test@mail.com", "test.com", "test_pass") == True
    assert show("pytest.db", "test", "test_app") == [('test_app', 'test_name', 'test@mail.com', 'test.com', 'test_pass')]
    assert check_exist("pytest.db", "test", "test_app") == True
    assert check_exist("pytest.db", "test", "test_appPPPPPPPP") == False
    os.remove("pytest.db")
