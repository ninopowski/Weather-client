#LWSK
import requests

def main():
    # print the header
    print_header()

    # get post code from user
    post_code = input("For what post code do you want a forecast?")

    # get html from web
    html = get_html_from_web(post_code)

    # parse the html
    # display the forecast


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


if __name__ == '__main__':
    main()

