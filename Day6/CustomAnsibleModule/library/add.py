#!/usr/bin/python

from ansible.module_utils.basic import *; 

class Adder:

    def add (self, firstValue, secondValue ):
        return firstValue + secondValue

def main():
    module = AnsibleModule (
            argument_spec = dict (
                    firstInput = dict ( required=True, type='int' ),
                    secondInput = dict ( required=True, type='int' )
                )
    );

    firstNumber = module.params['firstInput']
    secondNumber = module.params['secondInput']

    addObj = Adder()

    result = { "Result": str(addObj.add ( firstNumber, secondNumber )) }

    #module.exit_json ( changed=True, meta=result )
    module.fail_json ( 'Fatal error occured' )

main()

