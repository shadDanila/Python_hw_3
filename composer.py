import collections as col
import numpy as np


def compose(sentence_begin, sentence_end, second_word, third_word, sentence_length, length):
    story = open('my_story.txt', 'w')
    sentence_begin_flag = 0
    st = []
    index = 0
    end_flag = False
    while index < length:
        rand_value = np.random.uniform(0, 1, 1)
        total = 0.0
        if sentence_begin_flag == 0:
            rand_length = np.random.uniform(0, 1, 1)
            for size in sentence_length:
                if not size == 0:
                    total += float(sentence_length[size])/sentence_length[0]
                    if total > rand_length:
                        current_length = 3 + int(size)
                        total = 0.0
                        break
            for word in sentence_begin:
                if not word == 0:
                    total += float(sentence_begin[word])/sentence_begin[0]
                    if total > rand_value:
                        story.write(word)
                        index += 1
                        sentence_begin_flag = 1
                        st.append(word)
                        break
        elif sentence_begin_flag == 1:
            try:
                for word in second_word[st[-1]]:
                    if not word == 0:
                        total += float(second_word[st[-1]][word])/second_word[st[-1]][0]
                        if total > rand_value:
                            st.append(word)
                            sentence_begin_flag += 1
                            story.write(' ' + word)
                            index += 1
                            break
            except:
                sentence_begin_flag = 0
                st = []
                story.write('. ')
        elif sentence_begin_flag >= 2:
            try:
                for word in third_word[st[-2] + ' ' + st[-1]]:
                    if not word == 0:
                        total += float(third_word[st[-2] + ' ' + st[-1]][word])/(third_word[st[-2] + ' ' + st[-1]][0])
                        if total > rand_value:
                            st.append(word)
                            story.write(' ' + word)
                            index += 1
                            sentence_begin_flag += 1
                            break
            except:
                sentence_begin_flag = 0
                st = []
                story.write('. ')
        try:
            if current_length <= sentence_begin_flag and sentence_begin_flag > 0 and not sentence_end[st[-1]] == 0:
                sentence_begin_flag = 0
                st = []
                story.write('. ')
                if np.random.uniform(0, 1, 1) > 0.85:
                    story.write('\n\n')
        except:
            pass
        if index == length and sentence_begin_flag > 0:
            end_flag = True
            index -= 1
        if end_flag and sentence_begin_flag == 0:
            story.write('The end.')
            return


def main():
    sentence_begin = eval(open('sentence_begin.txt', 'r').read())
    sentence_end = eval(open('sentence_end.txt', 'r').read())
    second_word = eval(open('second_word.txt', 'r').read())
    third_word = eval(open('third_word.txt', 'r').read())
    sentence_length = eval(open('sentence_length.txt', 'r').read())

    compose(sentence_begin, sentence_end, second_word, third_word, sentence_length, 10000)
    

if __name__ == '__main__':
    main()
    