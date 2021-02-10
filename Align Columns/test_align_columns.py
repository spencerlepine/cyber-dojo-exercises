from align_columns import print_columns

text = "Given$a$text$file$of$many$lines,$where$fields$within$a$line\n$are$delineated$by$a$single$'dollar'$character,$write$a$program\n$that$aligns$each$column$of$fields$by$ensuring$that$words$in$each\n$column$are$separated$by$at$least$one$space.\n$Further,$allow$for$each$word$in$a$column$to$be$either$left\n$justified,$right$justified,$or$center$justified$within$its$column.\n"

def Atest_align_center(capsys):
    print_columns(text, "center")
    
    captured = capsys.readouterr()
    assert captured.out == "something"
    
def Atest_align_right(capsys):
    print_columns(text, "right")
    
    captured = capsys.readouterr()
    assert captured.out == "     Given          a       text       file         of       many     lines,      where     fields     within          a       line\n       are delineated         by          a     single   'dollar' character,      write          a    program\n      that     aligns       each     column         of     fields         by   ensuring       that      words         in       each\n    column        are  separated         by         at      least        one     space.\n  Further,      allow        for       each       word         in          a     column         to         be     either       left\njustified,      right justified,         or     center  justified     within        its    column.\n"
    
def test_align_left(capsys):
    print_columns(text, "left")
    
    captured = capsys.readouterr()
    
    assert captured.out == "Given      a          text       file       of         many       lines,     where      fields     within     a          line      \nare        delineated by         a          single     'dollar'   character, write      a          program   \nthat       aligns     each       column     of         fields     by         ensuring   that       words      in         each      \ncolumn     are        separated  by         at         least      one        space.    \nFurther,   allow      for        each       word       in         a          column     to         be         either     left      \njustified, right      justified, or         center     justified  within     its        column.   \n"