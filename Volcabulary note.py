#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os
import sys
from time import sleep
import random



def input_more(text):
    sys.stdout.write('Meaning: ')
    list_input = list()
    count = 0
    while True:
        __string_input = input()
        if __string_input == '':
            count = count + 1
        else:
            count = 0

        if count >= 2:
            break
        else:
            list_input.append(__string_input)
    rs = '\t'.join(list_input)[:-1]                 # ignore 2 enter to stop meaning cause \t at end
    return '\n'+rs


if __name__ == '__main__':

    path = ""
    # dictionary = 'dictionary.txt'
    dictionary = 'dict_IT.txt'


    while True:
        os.system('cls')
        string_input = input('Command:')


        # command STOP
        if string_input == 'q':
            break


        # command RANDOM
        command_pos = string_input.find('random')
        if command_pos > -1:
            with (open(path+dictionary, 'r' , encoding = 'utf-8')) as file_read:
                read_data = file_read.readlines()

            # Create ramdom list and slip on it
            random.shuffle(read_data)
            for _line in read_data:
                word = _line.split('\t')[0]
                mean = '\n'.join(_line.split('\t')[1:])

                os.system('cls')
                print('\n'+'ҳҲҳ'*20)
                print('\tWord:\t\t', word)
                input('\tYour answer: ')                                   # I want wait for brain runing before show mean
                print('-' * 50)
                [print('♥\t'+x) for x in mean.split('\n')]
                print('ҳҲҳ'*20 +'\n')
                input()


        # command ADD
        command_pos = string_input.find('add')
        if command_pos > -1:
            if string_input != 'add':                                                       # Pass add 0 Word
                meanning_input = input_more('Meaning that ! "q" to finish. ')
                with (open(path + dictionary, 'ab')) as file:
                    data_write = string_input[len('add'):].strip() + '\t' + meanning_input.strip() + '\n'
                    file.write(data_write.encode('utf-8'))
                
                print('Writed: '+data_write)
                input()


        # command SEARCH
        else:
            with open(path+dictionary , 'r' , encoding='utf-8' ) as file_read_search:
                data = file_read_search.readlines()

            isExit_word = False
            for _line in data:
                word = _line.split('\t')[0]                         # 1st-tab is seperated by word and mean
                mean = '\n'.join(_line.split('\t')[1:])             # Extand-tabs is multi mean separated by line

                # Search in mean and word , ignore ''
                if string_input == '':
                    break
                elif word.strip() == string_input.strip():              # Word is obsolutely accurate
                    isExit_word = True
                    print('\n'+'ҳҲҳ'*20)
                    print('♥\t' + word)
                    print('♥' + '-' * 48)
                    [print('♥\t'+x) for x in mean.split('\n')]
                    print('ҳҲҳ'*20 +'\n')
                    break

                elif word.find(string_input.strip()) > -1 :             # Word and mean is proximately likable
                    isExit_word = True
                    print('\n'+'ҳҲҳ'*20)
                    print('#\t' + word)
                    print('#' + '-' * 48)
                    [print('#\t'+x) for x in mean.split('\n')]
                    print('ҳҲҳ'*20 +'\n')

                elif mean.find(string_input.strip()) > -1 :             # Like upon but i want coding separation
                    isExit_word = True
                    print('\n'+'ҳҲҳ'*20)
                    print('#\t' + word)
                    print('#' + '-' * 48)
                    [print('#\t'+x) for x in mean.split('\n')]
                    print('ҳҲҳ'*20 +'\n')

            # Not found define Word
            if not isExit_word and string_input != '':
                print('Not found in dictionary')

            input()
