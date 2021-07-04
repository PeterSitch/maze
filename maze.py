import streamlit as st

##https://www.logicmazes.com/bureau/index.htm
# solution hr,cc,m,cc,im, hr
##         mum, reception,mr,reception, miss,mum

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
        st.markdown(f'## You have permission to go home!  \n You took {st.session_state.steps} moves')
        st.balloons()
    else:
        st.markdown("She's very sorry but can't take you home until you have permission.  \nShe suggests that you'll need to talk to either:")

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
    st.markdown(f"They shake their head and say you cannot go home yet.  \n"
                f"They suggest that you'll need to talk to {op_str}:")
    
    buttons(options)

def im(prev):

    #st.write('Welcom to im')

    if prev=='cc':
        options = ['m','hr']
    elif prev=='m' or prev=='hr':
        options = ['m','cc']
    st.markdown(f"They see that you have come from {flavour_dict[prev]} but still say you cannot go home yet.  \n"
                f"They suggest that you'll need to talk to either:")
    
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
    
    st.markdown("They say they are very sorry but you cannot go home yet.  \nThey suggest that you'll need to talk to:")

    buttons(options)

def buttons(options):
    for i, option in enumerate(options):
        st.button(flavour_dict[option], on_click=move,args=(option,)) 
        if i +1 != len(options):
            st.write('or')


loc_dict={'hr':hr,'m':m,'cc':cc,'im':im}

flavour_dict={'hr':'Mummy','m':'Mr Johnston','cc':'The nice receptionist','im':'Miss Randall'}
        
if 'prev' not in st.session_state:
	st.session_state.prev = 'start'
    
if 'loc' not in st.session_state:
	st.session_state.loc = 'hr'
if 'steps' not in st.session_state:
    st.session_state.steps=0

st.title ('School Bureaucracy Maze')


st.info("Welcome to the school bureaucracy maze.  \n You are trying to get permission to go home  \n You'll need to talk to lots of people")
    

st.markdown(f'## You are talking to {flavour_dict[st.session_state.loc]}')

if st.session_state.steps>20:
    st.markdown('You are very tired')

    
loc_dict[st.session_state.loc](st.session_state.prev)

