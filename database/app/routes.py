from flask import render_template
from app import application
from app.models import Winner

snap_winners = [
    Winner(spots="Tropical Grove"),
    Winner(spots="Sunken Garden"),
    Winner(spots="Hackett Cafe") 
]

fun_winners = [
    Winner(spots="Toga"),
    Winner(spots="Desi Ball"),
    Winner(spots="Sun-Downer"),
]

snap_award_names = ['Best Reviews', 'Solo Shoot', 'Best Vibe']

fun_award_names = ['Best Reviews', 'Worth it!' , 'Most Welcoming']

@application.route('/')
def index():
    snap_zipped_winners = zip(snap_winners, snap_award_names)
    fun_zipped_winners = zip(fun_winners, fun_award_names)
    return render_template('Awardspage-current.html', fun_zipped_winners=fun_zipped_winners, snap_zipped_winners=snap_zipped_winners)