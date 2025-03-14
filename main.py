import streamlit as st
import json

# load & save library data
def load_library():
    try:
        with open("library.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_library():
    with open("library.json", "w") as file:
        json.dump(library, file, indent=4)

# initialize library
library = load_library()

st.title("personal library manager")
menu = st.sidebar.radio("select an option",["view library","add books","remove books","search book","save and exit"])
if menu == "view library":
    st.sidebar.title("Your Library")
    if library:
        st.table(library)
    else:
        st.write("no books in your library, add some books!")

# add books
elif menu == "add books":
    st.sidebar.title("Add a New Book")
    title = st.text_input("title")
    author = st.text_input("author")
    year = st.number_input("year",min_value=2022,max_value=2100)
    catigery = st.text_input("catigery")
    read_status = st.checkbox("mark as read")

    if st.button("add book"):
        library.append({"title":title,"author":author,"year":year,"catigery":catigery,"read_status":read_status})
        save_library()
        st.success("book added successfully!")
        st.rerun()

#remove book
elif menu == "remove books":
    st.sidebar.title("Remove a Book")
    book_titles = [book["title"] for book in library]

    if book_titles:
        selected_book = st.selectbox("select a book to remove",book_titles)
        if st.button("remove book"):
            library = [book for book in library if book["title"] != selected_book]
            save_library()
            st.success("book remove successfully!")
            st.rerun()

        else :
            st.warning("no book in your library, add some books!")

# search book
elif menu == "search book":
    st.sidebar.title("Search a Book")
    search_term = st.text_input ("enter title or author name")

    if st.button("search"):
        results = [book for book in library if search_term.lower() in book
         ["title"].lower()or search_term.lower()in book["author"].lower()]
        if results:
            st.table(results)
        else :
            st.Warning("no book found")

# save and exit
elif menu == "save and exit":
    save_library()
    st.success("library saved successfully!")
    