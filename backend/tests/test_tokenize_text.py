from application.modules.words.functions import tokenize_text

def test_string_is_empty():
    result = tokenize_text("")
    assert type(result) is list
    assert len(result) == 0

def test_string_only_special_characters():
    result = tokenize_text("$# () .. ; , -- = ++ >= ...")
    assert type(result) is list
    assert len(result) == 0

def test_string_tokenize():
    result = tokenize_text("""
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla mauris ipsum, efficitur id 
        risus in, malesuada luctus magna. Praesent lorem dolor, venenatis et consequat vel, rhoncus 
        eget enim. In fermentum mattis urna, ut posuere tortor vulputate at. Sed fringilla, risus non
        viverra lacinia, purus sapien luctus purus, sit amet iaculis sapien sapien ut quam. Nam 
        ultrices metus nisl, sed pulvinar ante suscipit ac. Curabitur vel pharetra arcu, ac lacinia 
        nulla. Suspendisse vitae elit consequat dui iaculis auctor. Nunc ultrices ut turpis quis 
        dignissim. Nunc eu interdum arcu, commodo bibendum ipsum. Aliquam in metus vitae velit
        egestas maximus nec a justo.""")
    assert type(result) is list
    assert len(result) == 101

def test_string_tokenize_special_characters():
    result = tokenize_text("""
        ()Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla mauris ipsum, efficitur id 
        risus in, malesuada luctus magna. ++ Praesent lorem dolor, venenatis et consequat vel, rhoncus 
        eget enim. In fermentum mattis urna, ut psuerê tortor vulputate at. Sed fringilla, risus non
        viverra lacinia, purus sapien luctus \n () purus, sit amet iaculis sapien sapien ut quam. Nam 
        ultrices metus nisl, sed pulvinar ante suscipit ac. Curabitur vel pharetra arcu, ac lacinia 
        nulla. Suspendisse vitae elit consequat dui iaculis auctor. Nunc ultrices ut turpis quis 
        dignissim. Nunc eu interdum arcu, commodo bibendum ipsum. Aliquam in metus vitae velit
        egestas maximus nec a justo. >=""")
    assert type(result) is list
    assert len(result) == 101