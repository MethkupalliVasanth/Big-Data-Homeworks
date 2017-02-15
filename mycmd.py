from __future__ import print_function, division
import cmd

#deploy kill benchmark report

class Calculator(cmd.Cmd):
	prompt = 'cmd > '
	intro = 'mycmd file'

	def do_deploy(self, line):
		args = line.split()
		print('deploy')
		print('args: ', end='')
		for arg in args:
			print(arg.strip(), end=' ')
		print()

	def help_deploy(self):
		print('Deploy command')

	def do_kill(self, line):
		args = line.split()
		print('kill')
		print('args:', end='')
		for arg in args:
			print(arg.strip(), end=' ')
		print()

	def help_kill(self):
		print('Kill command')
	
	def do_benchmark(self, line):
		args = line.split()
		print('benchmark')
		print('args: ', end='')
		for arg in args:
			print(arg.strip(), end=' ')
		print()

	def help_benchmark(self):
		print('Benchmark command')
	
	def do_report(self, line):
		args = line.split()
		print('report')
		print('args: ', end='')
		for arg in args:
			print(arg.strip(), end=' ')
		print()

	def help_report(self):
		print('Report command')
	
	def do_EOF(self, line):
		print('bye, bye')
		return True
	
	def help_EOF(self):
		print('Exits the program.')

if __name__ == '__main__':
	Calculator().cmdloop()
