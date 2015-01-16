from main import app
from flask import render_template, request
from config import FREEZER_BASE_URL


@app.route('/')
def index():
    page_title = "Gov. Peter Shumlin's 2015 Budget Address"
    page_url = FREEZER_BASE_URL.rstrip('/') + request.path

    social = {
        'title': "Interactive Audio Transcript: Gov. Peter Shumlin's 2015 Budget Address",
        'subtitle': 'In part two of what Shumlin called his "Agenda for Progress," Shumlin outlined his budget priorities, including an increase in payroll taxes for Vermont businesses.',
        'img': "http://www.vpr.net/apps/interactive-transcript-gov-peter-shumlins-2015-budget-speech/static/img/shumlin-budget-ap-duback-20150115.jpg",
        'description': 'In part two of what Shumlin called his "Agenda for Progress," Shumlin outlined his budget priorities, including an increase in payroll taxes for Vermont businesses.',
        'twitter_text': "Interactive Transcript: @GovPeterShumlin's 2015 budget address by @avtransc",
        'creator': "Averbach Transcription and VPR News Staff",
        'twitter_hashtag': "vtpoli"
    }

    return render_template('content.html',
        page_title=page_title,
        page_url=page_url,
        social=social)
