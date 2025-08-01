'''WAF to read the text from a given 'poem.text' and find out whether it contains the wprd twinkle'''
with open("poem.txt") as f:
    st = f.read()
    print(st)
    if ( "twinkle" in st.lower()):
      print("Twinkle on this file")
    else:
      print("not word there")