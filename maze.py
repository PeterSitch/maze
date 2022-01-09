import streamlit as st
#from PIL import Image

##https://www.logicmazes.com/bureau/index.htm
# solution hr,cc,m,cc,im, hr
##         owl, basket,kara_nala,basket, head min,owl

st.set_page_config(
    page_title="Meredith maze",
    page_icon="🦊",
    layout="centered",

 )


def move (option):
    st.session_state.prev=st.session_state.loc
    st.session_state.loc=option
    st.session_state.steps +=1


def hr(prev):
    
    #st.write('Welcom to hr')
    
    if prev=='start':
        options = ['m','cc']
    elif prev=='m':
        options = ['cc','im']
    
    elif prev=='cc':
        options = ['m','im']
        
    if prev=='im':
        ##options = ['win']
        col1.markdown(f'## Woo Hoo! You have escaped the maze!  \n You took {st.session_state.steps} moves')
        col2.image('winner.jpg',use_column_width ='always')
        st.balloons()
        st.session_state.loc = 'win'
    else:
    
        col2.image('wise_old_owl.jpg',use_column_width ='always')
    
        col1.markdown("She's very very sorry but she can't let you escape until you have successfully cracked the maze.  \n"
                        "She suggests that you'll want to visit either:")

        buttons(options)


def m(prev):
    
    #st.write('Welcom to m')

    if prev=='cc':
        options = ['cc','im','hr']
    elif prev=='im':
        options = ['hr']
    elif prev=='hr':
        options = ['im']
    if len(options)>1:
        op_str = 'either'
    else:
        op_str = ''
        
    col1.markdown(f"They shake their heads. Dear, oh dear. You cannot escape yet.  \n"
                f"They suggest that you'll want to visit {op_str}:")
    col2.image('kara_nala.jpg',use_column_width ='always')
    
    buttons(options)

def im(prev):

    #st.write('Welcom to im')

    if prev=='cc':
        options = ['m','hr']
    elif prev=='m' or prev=='hr':
        options = ['m','cc']
    col1.markdown(f"They see that you've come from {flavour_dict[prev][1]} but shake their head when you ask if you can escape.  \n"
                f"They growl under their breath, then turn to you and, with some displeasure, gesture wildly in the direction of:")
    col2.image('head_minion.jpg',use_column_width ='always')            
    
    buttons(options)
            
            
def cc(prev):
    #st.session_state.loc=='cc'
    #st.write('Welcom to cc')

    if prev=='m':
        options = ['im','hr']
    elif prev=='im':
        options = ['m','hr']
    elif prev=='hr':
        options = ['m']
    
    if len(options)>1:
        op_str = 'either'
    else:
        op_str = ''
    
    col1.markdown(f"Dogman's cheeks turn red and his tail darts between his legs.  \n   He didn't expect the maze to lead to his bedroom in such a mess. \n"
                    f"The Crimson Vixen politely pretends not to notice and suggests visiting {op_str}:")
    
    col2.image('dogman_basket.jpg',use_column_width ='always')
    
    buttons(options)

def buttons(options):
    for i, option in enumerate(options):
        col1.button(flavour_dict[option][1], on_click=move,args=(option,)) 
        if i +1 != len(options):
            col1.write('or')


loc_dict={'hr':hr,'m':m,'cc':cc,'im':im}

flavour_dict={'hr':('at the tree of life talking to', 'The Wise Old Owl'),
              'm':('hanging out with', 'Kara and Nala'),
              'cc':('at', 'Dogman\'s basket'),
              'im':('stopped by', 'Dogman\'s Head Minion')}
        
if 'prev' not in st.session_state:
	st.session_state.prev = 'start'
    
if 'loc' not in st.session_state:
	st.session_state.loc = 'hr'
if 'steps' not in st.session_state:
    st.session_state.steps=0

st.title ('🦊 Meredith\'s Maze')


st.info("Welcome to the Meredith's maze.  \n"+
 "The Crimson Vixon and Dogman are trying to puzzle through the maze.  \n"+
 "They haven't been able to find a map so they'll need to do lots of exploring, and visit the locations in just the right order")
    
col1,col2 = st.beta_columns(2)

col1.markdown(f'## You are {flavour_dict[st.session_state.loc][0]} {flavour_dict[st.session_state.loc][1]}')

    
loc_dict[st.session_state.loc](st.session_state.prev)

if st.session_state.loc != 'win':
    if st.session_state.steps>20:
        st.markdown(f"The Crimson Vixon and Dogman are getting very tired  \n So far they've been to {st.session_state.steps} locations!")
        st.image('tired_heros.jpg',use_column_width ='always')