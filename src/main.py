import streamlit as st
import levenshtein_distance as ld

if __name__ == '__main__':
    st.title('Word Correction')
    word = st.text_input("Your Word")
    vocabs = ld.load_vocab(
        r"D:\Github\AIO_project\Word-Correction\data\vocab.txt")

    if st.button('Compute'):
        distances = dict()
        for vocab in vocabs:
            distance = ld.levenshtein_distance(word, vocab)
            distances[vocab] = distance
        sorted_distances = sorted(distances.items(), key=lambda x: x[1])
        correct_word = sorted_distances[0][0]
        st.write('Correct word: ', correct_word)
