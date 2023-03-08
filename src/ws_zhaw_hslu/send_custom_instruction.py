import compas_rrc as rrc

if __name__ == '__main__':

    # Create Ros Client
    ros = rrc.RosClient()
    ros.run()

    # Create ABB Client
    abb = rrc.AbbClient(ros, '/rob1')
    print('Connected.')

    # Custom instruction name (RAPID Procedure name)
    # instruction = 'r_WS_MoveToHome'
    # instruction = 'r_WS_MoveToZero'
    # instruction = 'r_WS_GetVacuum'
    # instruction = 'r_WS_PlaceVacuum'
    instruction = 'r_WS_PlaceVacuum'

    # string vlaue list of 8 strings
    string_values = []

    # float value list of 36 floats
    float_values = []

    # Custom instruction
    done = abb.send_and_wait(rrc.CustomInstruction(instruction, string_values, float_values))

    # Print feedback
    print('Feedback = ', done)

    # End of Code
    print('Finished')

    # Close client
    ros.close()
    ros.terminate()
