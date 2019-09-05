import requests
import os
from time import sleep as sp
import json

mov_url_json = 'https://yts.lt/api/v2/list_movies.json?limit='
search_url = 'https://yts.lt/api/v2/list_movies.json?query_term='


class color:
    pink = '\033[95m'
    purple = '\33[35m'
    orange = '\033[33m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    end = '\033[0m'


class TorrentyPy:

    @staticmethod
    def mov_list(limit):

        r = requests.get(mov_url_json + str(limit))
        if r.status_code == 200:
            print('\nPlease Wait Getting Data.')
            with open('.temp.json', 'w') as js:
                json.dump(r.json(), js)

            mov = json.load(open('.temp.json', 'r'))
            print("\n\t\tMovies List\n")
            for i in mov["data"]["movies"]:
                print('**************************************')
                print('Name          : ' + i["title_english"])
                print('URL           : ' + i["url"])
                print('Genre         :' + str(i["genres"]))
                print('Year Released : ' + str(i["year"]))
                print("Rating        : " + str(i["rating"]))
                print('Total Time    : ' + str(i["runtime"]))
                print('\n')

    @staticmethod
    def search(query):

        r = requests.get(search_url + str(query))
        with open('.temp.json', 'w') as js:
            json.dump(r.json(), js)

        mov = json.load(open('.temp.json', 'r'))

        if mov["status_message"] == "Query was successful":
            print("\nSearch Successfull.\n")
            for i in mov["data"]["movies"]:
                print('**************************************')
                print('Name          : ' + i["title_english"])
                print('URL           : ' + i["url"])
                print('Genre         :' + str(i["genres"]))
                print('Year Released : ' + str(i["year"]))
                print("Rating        : " + str(i["rating"]))
                print('Total Time    :' + str(i["runtime"]))
                print('\n')

                query = query.replace(' ', '-')

                a = input('\nDo U Wish To Download Torrent[y/N]: ').lower()
                if a == 'y':
                    for k in i["torrents"]:
                        global url
                        url = str(k["url"])
                        url = url.replace("\\", '')
                    print('\nDownloading Torrent File\n')

                    if os.path.exists('TorrentyPy/downloads'):
                        pass
                    else:
                        os.system('mkdir TorrentyPy')
                        os.system('mkdir TorrentyPy\downloads')

                    os.system('cd TorrentyPy\downloads && wget --output-document ' + query + '.torrent ' + url + ' -nv')

                else:
                    sp(1)
                    return main()

        else:
            print("Movie Not Found...")

    @staticmethod
    def chk_movies(movies_list):

        if os.path.exists(movies_list):
            pass
        else:
            raise FileNotFoundError

        if os.path.exists('TorrentyPy'):
            pass
        else:
            os.system('mkdir TorrentyPy')

        with open(movies_list, 'r') as movie_list:
            for line in movie_list:
                line = line.strip('\n')

                r = requests.get(search_url + str(line))
                with open('.temp.json', 'w') as js:
                    json.dump(r.json(), js)

                mov = json.load(open('.temp.json', 'r'))
                if mov["status_message"] == "Query was successful":
                    res = line + "\t\t--Movie Found.\n"
                    print(res)

                    if os.path.exists('\TorrentyPy\TorrentyPy_res.txt'):
                        with open('TorrentyPy\TorrentyPy_res.txt', 'a') as results:
                            results.write(res)

                    else:

                        os.system('type NUL > TorrentyPy\TorrentyPy_res.txt')
                        with open('TorrentyPy\TorrentyPy_res.txt', 'a') as results:
                            results.write(res)

                else:
                    print(line + "\t\t--Movie Not Found.\n")

    @staticmethod
    def chk_down(movies_list):

        if os.path.exists(movies_list):
            pass
        else:
            raise FileNotFoundError

        if os.path.exists('TorrentyPy'):
            pass
        else:
            os.system('mkdir TorrentyPy')

        with open(movies_list, 'r') as movie_list:
            for line in movie_list:
                line = line.strip('\n')

                r = requests.get(search_url + str(line))
                with open('.temp.json', 'w') as js:
                    json.dump(r.json(), js)

                mov = json.load(open('.temp.json', 'r'))
                if mov["status_message"] == "Query was successful":
                    print('\n' + line + "\t\t--Movie Found.\n")
                    print('Downloading Torrent Please Wait...\n')

                    line = line.replace(' ', '-')

                    for i in mov["data"]["movies"]:
                        for k in i["torrents"]:
                            global url

                            url = str(k["url"])
                            url = url.replace("\\", '')
                        if os.path.exists('TorrentyPy/downloads'):
                            pass
                        else:
                            os.system('mkdir TorrentyPy/downloads')

                    os.system('cd TorrentyPy\downloads && wget --output-document ' + line + '.torrent ' + url + ' -nv')
                else:
                    print(line + "\t\t--Movie Not Found.\n")

            sp(1)
            print('\n\nAll The Files Have Been Downloaded To TorrentyPy\downloads')


def main():
    print('\n\t\tMENU\n')
    print('1.Get Latest Movie List.')
    print('2.Search For A Movie.')
    print('3.Perform Mass Movie Search.')
    print('4.Download Huge List Of Torrent Files.')
    print('5.Exit.')

    opt = input('\nEnter Your Choice: ')

    if opt == '1':
        print('\nGetting A Fresh Movie List Please Wait..')
        TorrentyPy.mov_list(20)
        os.system('del .temp.json')
        sp(2)
        input('\nPress Enter Key To Continue...')
        return main()

    elif opt == '2':
        query = input('\nMovie To Search: ')
        TorrentyPy.search(query=query)
        os.system('del .temp.json')
        sp(2)
        input('\nPress Enter Key To Continue...')
        return main()

    elif opt == '3':
        print('\nInitiating The Searcher Please Wait...\n')
        TorrentyPy.chk_movies(movies_list='movie_list.txt')
        os.system('del .temp.json')
        sp(2)
        return main()

    elif opt == '4':
        print('\nInitiating The Downloader Please Wait...\n')
        TorrentyPy.chk_down(movies_list='movie_list.txt')
        os.system('del .temp.json')
        sp(2)
        return main()

    elif opt == '5':
        print('\nSorry To See You Go..\n')
        sp(2)
        exit(0)

    else:
        print('\nUnknow Option Selected.Please Retry...')
        sp(2)
        return main()


if __name__ == '__main__':
    print('''
        _____                               _          ______       
       |_   _|                             | |         | ___ \      
         | |  ___   _ __  _ __  ___  _ __  | |_  _   _ | |_/ /_   _ 
         | | / _ \ | '__|| '__|/ _ \| '_ \ | __|| | | ||  __/| | | |
         | || (_) || |   | |  |  __/| | | || |_ | |_| || |   | |_| |
         \_/ \___/ |_|   |_|   \___||_| |_| \__| \__, |\_|    \__, |
                                                   _/ |        __/ |
                                                  |___/        |___/ 
                                  Torrent CLI Client by 41_alderson
    ''')
    sp(1.5)

    print('''
    \t\tAuthor:   41_alderson
    \t\tGithub:   https://github.com/41alderson/TorrentyPy
    \t\tTelegram: @destroyer41 
    \nIf You Find Any Problem Or Want Any New Feature To Be Added To The Script
Please Pull A New Request On Github (Or) Contact Me.''')

    sp(1.5)

    print(
        '''\n\nNote1: Currently Its Gets Top 20 Movie List.If You Want To get More Movie List Change The Limit In The Script.\n\n'''
        + '''Note2: To Perform Mass Movie Search Or Mass Download Please Keep Rename The txt Containing The list Of The Movies as \'movie_list.txt\' And Make Sure Both Script And File are In Same Folder.''')
    sp(1)

    main()