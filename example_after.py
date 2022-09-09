

class Example:
    # ====================================================================================#
    #                                      constructor                                     #
    # ====================================================================================#

    def __init__(self):
        self.line_size=25
    # ====================================================================================#
    #                                      PRINT BLOCK                                     #
    # ====================================================================================#

    def print_first_text(self):
        print('text 1')
        print('text was printed')

    def print_second_text(self):
        print('text 2')
        print('text was printed')

    # ====================================================================================#
    #                                      STUPID LOOP                                     #
    # ====================================================================================#

    def make_hard_loop(self):
        line=[]
        for i in range(self.line_size):
            line.append(' ')
        for i in range(len(line)):
            line[i]=i
        print(line)
        return line

    # ====================================================================================#
    #                               I DONT KNOW WHAT IS THIS                              #
    # ====================================================================================#

    def qwertyuiop(self):
        line=[[[[]]]]
        for i in 'asdfghjkl;':
            for j in 'zxcvbnm,./':
                print('USE BEAUTY COMMENTS')

    # ====================================================================================#
    #                                     LAST EXAMPLE                                    #
    # ====================================================================================#

    def last_example(self):
        e=str(['e'])
        x=str(['x'])
        a=str(['a'])
        m=str(['m'])
        p=str(['p'])
        l=str(['l'])
        e=str(['e'])
        line=''.join([e, x, a, m, p, l, e])
        line=line.replace('[','')
        line=line.replace(']','')
        line=line.replace('\'','')
        print(line)

if __name__ == '__main__':
    example=Example()
    example.last_example()



