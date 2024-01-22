import streamlit as st
import time

#Page Title
st.set_page_config(page_title="Flames",page_icon=":❤️:")

#Sidebar
#About 
st.sidebar.title(":green[About]")
st.sidebar.write('''
                    :gray[
                            Discover the chemistry in your relationship with the Flames game - a brief and entertaining way to assess compatibility and explore the unique dynamics that make your connection special
                    ]
                 ''')

#About Developer
st.sidebar.markdown("---")
st.sidebar.title(":green[About Developer]")
st.sidebar.write(":gray[This web application is developed by :violet[Keerthivasan S J]]")

#Contact information
st.sidebar.title(":green[Reach out]")
st.sidebar.write(":blue[**:orange[Email]** : keerthivasan.cs22.krct.ac.in]")


#Flames Logic
def flames(name1,name2):
    name1 = name1.strip().lower().replace(" ", "")
    name2 = name2.strip().lower().replace(" ", "")
    for char in name1:
        if char in name2:
            name1 = name1.replace(char, "", 1)
            name2 = name2.replace(char, "", 1)

    length=len(name1+name2)
    print(name1+name2,length)
    relation=["FRIEND","LOVE","AFFECTION","MARRIAGE","ENEMY","SISTER"]

    while len(relation)>1:
        print(relation)
        result=length%len(relation)-1
        if result>=0:
            right=relation[result+1:]
            left=relation[:result]
            relation=right+left
        else:
            relation=relation[:result]
    print(relation)
    return length,relation[0]

#Main window
st.title(":green[Flames] Game ❤️")
successmessage=st.empty()
bname=st.text_input("**Your Name** ")
gname=st.text_input("**Partner Name**")
if st.button(":orange[Submit]"):
    if(len(bname) and len(gname)):
        message=""
        result=flames(bname,gname)
        if result[1]=="FRIEND":
            message="You both are good friends🫂"
        elif result[1]=="LOVE":
            st.balloons()
            message="You both are lovers 💗"
        elif result[1]=="AFFECTION":
            message="You and your partners have good affection 🤞"
        elif result[1]=="MARRIAGE":
            message="You and your partner will get married soon💍"
        elif result[1]=="ENEMY":
            message="Don't take it serious it's just a game😇"
        elif result[1]=="SISTER":
            message="You both are good brother and sisters 🧑‍🤝‍🧑"

        st.header(f":violet[{result[0]}] Character differ from both name")
        st.title(f"Your Relation :red[{result[1]}]")
        st.write(message)
        successmessage.success("Result genarated successfully",icon="✔️")
    else:
        successmessage.warning("Please enter the names befor submiting!",icon="⚠️")

    
