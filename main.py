from js import document

has_flipped_card = False
has_both_flipped_cards = False
lockboard = False
first_card = None
first_card_id = None
second_card = None
second_card_id = None


def flip_card(event):
    global has_flipped_card, has_both_flipped_cards, lockboard
    global first_card, first_card_id
    global second_card, second_card_id
    print("FLIP_CARD")
    if has_both_flipped_cards:
        unflip_cards()
    if lockboard:
        return
    card = event.currentTarget
    card.classList.add('flip')
    evaluate(event)


def evaluate(event):
    global has_flipped_card, has_both_flipped_cards
    global first_card, first_card_id
    global second_card, second_card_id

    print("EVALUATE")
    if not has_flipped_card:
        has_flipped_card = True
        first_card = event.currentTarget.dataset.framework
        first_card_id = event.currentTarget.id
    else:
        second_card_id = event.currentTarget.id
        if first_card_id == second_card_id:
            print(f'You chose the same card, please pick another')
            second_card_id = None
        else:
            second_card = event.currentTarget.dataset.framework
            second_card_id = event.currentTarget.id
            has_both_flipped_cards = True
            check_for_match()


def check_for_match():
    global has_both_flipped_cards
    global first_card, first_card_id
    global second_card, second_card_id

    print("CHECK_FOR_MATCH")
    if first_card == second_card and first_card_id != second_card_id:
        print("It's a match!")
        disable_cards()
        reset_board()
    else:
        print("Not a match")


def disable_cards():
    global first_card_id, second_card_id

    print("DISABLE_CARDS")
    document.getElementById(f"{first_card_id}").removeAttribute('py-click')
    document.getElementById(f"{second_card_id}").removeAttribute('py-click')
    first_card_id = None
    second_card_id = None


def unflip_cards():
    global has_flipped_card, has_both_flipped_cards, lockboard
    global first_card, first_card_id
    global second_card, second_card_id

    print("UNFLIP")
    lockboard = True
    document.getElementById(f"{first_card_id}").classList.remove('flip')
    document.getElementById(f"{second_card_id}").classList.remove('flip')
    lockboard = False
    reset_board()


def reset_board():
    global has_flipped_card, has_both_flipped_cards, first_card, first_card_id, second_card, second_card_id
    has_flipped_card = False
    has_both_flipped_cards = False
    first_card = None
    first_card_id = None
    second_card = None
    second_card_id = None
