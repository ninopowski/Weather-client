#LWSK
import requests
import bs4
import collections

WeatherInfo = collections.namedtuple("WeatherInfo",
                                     "condition, temperature")

def main():
    # print the header
    print_header()

    # get post code from user
    post_code = input("For what post code do you want a forecast?")

    # get html from web
    html = get_html_from_web(post_code)

    # parse the html
    report = get_weather_from_html(html)

    # display the forecast
    show_weather(report.condition, report.temperature)

def print_header():
    print("---------------------")
    print("---- WEATHER APP ----")
    print("---------------------")
    print()


def get_html_from_web(post_code):
    url = f"https://www.wunderground.com/weather/{post_code}"
    response = requests.get(url)
    #print(response.status_code)
    return response.text


def get_weather_from_html(html):
    location_css = ""
    weather_condition_css = "div.condition-icon p"
    temperature_css = "span.wu_value"

    soup = bs4.BeautifulSoup(html, 'html.parser')
    condition = soup.find(name="div", class_="condition-icon").get_text()
    temperature = soup.find(name="span", class_="temp").get_text()
    report = WeatherInfo(condition=condition, temperature=temperature)
    return report

def show_weather(cond, temp):
    print(f"Today at LWSK the conditions are {cond} and it feels like {temp}")








if __name__ == '__main__':
    main()

