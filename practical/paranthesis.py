#paranthesis matching or delimeter matching
from module.stacks import Stack

def checkParan(strg:str):
    st = Stack()
    openParan = "({[<"
    closeParan = ")}]>"
    for i in strg:
        if(i in openParan):
            st.push(i)
        elif(i in closeParan):
            try:
                if((i==')'and st.peek()=='(') or (i=='}'and st.peek()=='{') or (i==']'and st.peek()=='[') or (i=='>'and st.peek()=='<')):
                        st.pop()
                else:
                    print("Not Valid")     
                    return   
            except Exception as e:
                print("Not Valid")
                return
    if(st.len>0):
        print("Not Valid")
        return
    else:
        print("Valid")
        return
    
pran = "(({}()()[{}]))"
checkParan(pran)
checkParan("""<html>
                <head>
                    <link  href="">

                </head>
                <body>
                    <a href=""></a>      
                </body>

           </html>""")