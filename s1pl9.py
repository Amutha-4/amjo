def camelCase(st):
    Output = ''.join(x for x in st.title() if x.isalnum())
    return Output[0].lower() + Output[1:]
