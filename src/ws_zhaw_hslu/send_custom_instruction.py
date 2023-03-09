import compas_rrc as rrc

if __name__ == '__main__':

    # Create Ros Client
    ros = rrc.RosClient()
    ros.run()

    # Create ABB Client
    abb = rrc.AbbClient(ros, '/rob1')
    print('Connected.')

    # Custom instruction name (RAPID Procedure name)
    # Implemented instructions:
    # 'r_WS_MoveToHome'
    # 'r_WS_MoveToZero'
    # 'r_WS_GetVacuum'
    # 'r_WS_PlaceVacuum'
    # 'r_WS_OpenVacuumGripper'
    # 'r_WS_CloseVacuumGripper'

    instruction = 'r_WS_OpenVacuumGripper'


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
