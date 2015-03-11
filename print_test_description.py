import texttable as tt

tab = tt.Texttable()

x = [[]] # The empty row will have the header


x = [[],
     [1, '','','Create user1'],
     [2, '','','Create user2'],
     [3, 'Create folder\n test','',''],
     [4, 'Share test with user2\nWithout update permission','',''],
     [5, '','login',''],
     [6, '','Share test\nwith link',''],
     [7, '','Allow editing',''],
     ]



tab.add_rows(x)
tab.set_cols_align(['r','r','r','r'])
tab.header(['Step Number', 'user1', 'user2', 'Admin'])
print tab.draw()

