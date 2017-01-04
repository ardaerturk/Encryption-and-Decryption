"""
Encrypt or decrypt the contents of a message file using a deck of cards.
"""

import cipher_functions

DECK_FILENAME = 'deck1.txt'
MSG_FILENAME = 'message-decrypted.txt'
MODE = 'e'  # 'e' for encryption, 'd' for decryption.


def main():
    """ () -> NoneType

    Perform the encryption using the deck from a file called DECK_FILENAME and
    the messages from a file called MSG_FILENAME. If MODE is 'e', encrypt;
    otherwise, decrypt. Print the decrypted message to the screen.
    REQ: A valid card_deck is a max of 26 cards and JOKER1 and JOKER2
    """
    # open the deck file
    file_deck = open(DECK_FILENAME, 'r')
    # read only the integer contents of the file
    read_deck = cipher_functions.read_deck(file_deck)
    # open the messages file
    file_messages = open(MSG_FILENAME, 'r')
    # Read the contents of the file as a list of messages.
    read_messages = cipher_functions.read_messages(file_messages)
    # If the mode is 'e' then encrypt. If the mode is 'd' then decrypt.
    encrypt_or_decrypt = cipher_functions.process_messages(read_deck,
                                                           read_messages, MODE)
    # close the files
    file_deck.close()
    file_messages.close()
    for element in range(len(encrypt_or_decrypt)):
        print(encrypt_or_decrypt[element])

main()