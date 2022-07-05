import numpy as np


A = np.random.randint(0,20, size=(4,12))
def pythonToLatex(array, type=[], equation_form='$' ):
	""" Type : 'parenthese'
		   'bracket' 
		   'vertical line' 
		   'double vertical lines'
		   'angle'
		   'ceil'
		   'none'
	"""
	""" Equation form : 
		Latex form (centering) with $$ ... $$ -> '$$'
		Latex form (no centering) with $ ...$ -> '$'
		Latex form with equation with \begin{equation} ... -> 'equation'
		Latex form with equation with \begin{equation*} ... -> 'equation_star'
	"""
	
	
	dict_type = {
	'parenthese': ['(',')'], 
	'square' : ['[',']'],
	'curly' : ['\{', '\}'],
	'vertical line' : ['|','|'],
	'double vertical lines' : ['||','||'],
	'angle' : ['\langle','\\rangle'],
	'ceil' : ['\lceil', '\\rceil'],
	'floor': ['\lfloor', '\\rfloor'],
	'none' : ['.', '.']
	}
	
	dict_equation_form = {
	'$' : ['$', '$'],
	'$$' : ['$$','$$'],
	'equation' : ['\\begin{equation}', '\label{eq:eqName}\n\end{equation}'],
	'equation_star': ['\\begin{equation*}', '\end{equation*}']
	}
	
	#### Brackets 
	if len(type)==2:
		begin_left = '\left'+dict_type[type[0]][0]
		begin_right = '\\right'+dict_type[type[1]][1]
	elif len(type)==1: 
		begin_left = '\left'+dict_type[type[0]][0]
		begin_right = '\\right'+dict_type[type[0]][0]
	else:
		print('The size of the type list should be 1 or 2')
	
	
	
	
	f = open('results.txt', 'w')
	### Left side 
	f.write(dict_equation_form[equation_form][0])
	f.write('\n')
	f.write(begin_left)
	f.write('\n')
	f.write('\\begin{matrix}')
	f.write('\n')
		
	### Matrix	
	x, y = array.shape[0], array.shape[1]
	for l, j in zip(array, range(x)) : 
		for c,i in zip(l, range(l.shape[0]-1)) : 
			f.write('{:.2f}'.format(c))
			f.write(' & ')
		f.write('{:.2f}'.format(l[-1]))
		if j+1 != x: 
			f.write(' \\')
			f.write('\\')
		f.write('\n')
			
			
	### Right side	
	f.write('\end{matrix}')
	f.write('\n')
	f.write(begin_right)
	f.write('\n')
	f.write(dict_equation_form[equation_form][1])
	f.close()
	
					
pythonToLatex(A, type= ['square', 'parenthese'], equation_form='equation')
