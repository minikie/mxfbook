import repository as repo


# usage
ws_name1 = 'ws'

print('variable load..............')
variable = repo.get_variable('ws', 'newVar')
print(variable)

print('variable value data load..............')
print variable.value()

print('')
print('---------------------------------')
print('')

print('all variable load..............')
variables  = repo.get_all_variables(workspace='ws')
print(variables)

for v in variables:
    print v.value()

#repo.get_variable('ws', 'newVar')

#print( variabless)
