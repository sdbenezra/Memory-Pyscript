from js import document
from js import location
from js import localStorage
from random import random
from math import floor

has_flipped_card = False
has_both_flipped_cards = False
lockboard = False
first_card = None
first_card_id = None
second_card = None
second_card_id = None
matches = 0
current_score = 0
best_score = 0


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
    global current_score, best_score, matches

    print("CHECK_FOR_MATCH")
    if first_card == second_card and first_card_id != second_card_id:
        print("It's a match!")
        update_score()
        matches += 1
        print(f'MATCHES:   {matches}')
        if matches == 6:
            print("you won")
            if best_score > current_score or best_score == 0:
                best_score = current_score
                update_best_score()
        disable_cards()
        reset_board()
    else:
        print("Not a match")
        update_score()


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
    global has_flipped_card, has_both_flipped_cards, lockboard, first_card, first_card_id, second_card, second_card_id
    lockboard = False
    has_flipped_card = False
    has_both_flipped_cards = False
    first_card = None
    first_card_id = None
    second_card = None
    second_card_id = None


def shuffle():
    cards = document.querySelectorAll('.memory-card')
    for card in cards:
        randomPos = floor(random() * 12)
        card.style.order = randomPos


def score_setup():
    global current_score, best_score
    document.getElementById("current-score").innerHTML = current_score
    print(localStorage.getItem("best-score"))
    best_score_retrieved = localStorage.getItem("best-score")
    if best_score_retrieved is None:
        best_score = 0
        document.getElementById("best-score").innerHTML = 0
    else:
        best_score = int(best_score_retrieved)
        document.getElementById("best-score").innerHTML = best_score


def update_score():
    global current_score
    current_score += 1
    document.getElementById("current-score").innerHTML = current_score


def update_best_score():
    global best_score
    document.getElementById("best-score").innerHTML = best_score
    localStorage.setItem("best-score", f"{best_score}")


def reset(event):
    location.reload()


shuffle()
score_setup()
