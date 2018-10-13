from model.contact import Contact


#@pytest.mark.skip(reason="no way of currently testing this") # для отключение теста
def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test7777"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="new firstname1")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_modify_contact_header(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(middlename="test7777"))
#     old_contacts = app.contact.get_contact_list()
#     app.contact.modify_first_contact(Contact(middlename="new middlename1"))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
