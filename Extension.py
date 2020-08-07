name =input("Input the filename: ")
i=name.find('.')
i+=1
if name[i:]=='py':
    print("The extension of the file is:'python'")
elif name[i:]=='java':
    print("The extension of the file is:'java'")                                               
elif name[i:]=='cpp':                                           
    print("The extension of the file is:'c plus plus'")                                        
elif name[i:]=='c':                                                
    print("The extension of the file is:'c'")                                       
elif name[i:]=='ppt':
    print("The extension of the file is:'power point'")                                            
elif name[i:]=='pdf':                                            
    print("The extension of the file is:'pdf'")                                            
elif name[i:]=='doc':                                            
    print("The extension of the file is:'document(Word)'")                                            
elif name[i:]=='txt':                                            
    print("The extension of the file is:'text'")
else:
    print("I don't know what to print")                                                
                                            
