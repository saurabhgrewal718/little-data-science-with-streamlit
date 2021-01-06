import streamlit as st
import pandas as pd
from PIL import Image
import altair as alt


image = Image.open('dna.jpg')

st.image(image,use_column_width=True)

st.write("""
# DNA Nucleotide WEB app

this app counts the neuclotide count of the querry dna
***
""")


#the dna textbox to be painted now
#how? lets see! 
st.header('Enter the DNA sequence')

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area("Sequence Input",sequence_input,height=250)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)

st.write("""
***

""")

#input data 
st.header('INPUT DNA Query')
sequence

#Prints thje dna nucleotide count now
st.header('Output (DNA NUcleotide Count)')

#print Dictionary
st.subheader('1.Print Dictionary')
def dna_Count(seq):
    d=dict([
        ('A',seq.count('A')),
        ('T',seq.count('T')),
        ('G',seq.count('G')),
        ('C',seq.count('C'))
    ])
    return d

X = dna_Count(sequence)

X_label = list(X)
X_values = list(X.values())

X

#printing the text
st.subheader('2. Print Text')
st.write('there are '+ str(X['A'])+ ' adenine (A)')
st.write('there are '+ str(X['T'])+ ' thymine (T)')
st.write('there are '+ str(X['G'])+ ' guanine (G)')
st.write('there are '+ str(X['C'])+ ' cytosine (C)')


# display data frame
st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X,orient = 'index')
df = df.rename({0:'Count'},axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index':'Nucleotide'})
st.write(df)


# display bar chart sing the data frame crearted in the above one using the altiar lib(charts)
st.subheader('3. Display Bar Chart')
p = alt.Chart(df).mark_bar().encode(
    x='Nucleotide',
    y='Count',
)
p= p.properties(
    width = alt.Step(80)#width of the bar chart bars
)
st.write(p)



