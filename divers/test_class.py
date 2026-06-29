import type_class
from player import Player

def test_mage_add_mana_mocker(mocker):
    mage = type_class.Mage()
    sut = Player("guitou", mage)
    
    mocker.patch("type_class.Mage.add_mana", return_value=10)
    expected_value = 20
    sut.drink_potion()

    assert sut.mana_point == expected_value

def test_mage_delete_mana_mocker(mocker):
    mage = type_class.Mage()
    sut = Player("guitou", mage)

    mocker.patch("type_class.Mage.delete_mana", return_value = -7)
    expected_value = 3
    sut.use_spell()

    assert sut.mana_point == expected_value