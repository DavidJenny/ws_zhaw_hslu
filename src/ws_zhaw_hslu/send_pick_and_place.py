import compas_rrc as rrc
from compas.geometry import Frame
from compas.geometry import Point
from compas.geometry import Vector

if __name__ == '__main__':

    # Create Ros Client
    ros = rrc.RosClient()
    ros.run()

    # Create ABB Client
    abb = rrc.AbbClient(ros, '/rob1')
    print('Connected.')

    # string vlaue list of 8 strings, for custom instructions
    string_values = []

    # float value list of 36 floats, for custom instructions
    float_values = []


    # define pick position
    pick_safety_joints, external_axes = [-90.0, -25.0, 0.0, 0.0, 90.0, 0.0], []

    pick_position = Frame(Point(474.34, 74.42, 3.6), Vector(-1, 0, 0), Vector(0, 1, 0))
    pick_approach = Frame(Point(474.34, 74.42, 3.6 + 100), Vector(-1, 0, 0), Vector(0, 1, 0))



    # define place positions
    place_positions = []
    place_position_1 = Frame(Point(0, 0, 50), Vector(-1, 0, 0), Vector(0, 1, 0))
    place_position_2 = Frame(Point(50, 0, 50), Vector(-1, 0, 0), Vector(0, 1, 0))
    place_position_3 = Frame(Point(50, 50, 50), Vector(-1, 0, 0), Vector(0, 1, 0))
    place_positions.extend([place_position_1, place_position_2, place_position_3])

    # pick and place procedure
    # set tool to tVacuumSchmalz, Vacuum Gripper
    done = abb.send_and_wait(rrc.SetTool('tVacuumSchmalz'))

    # set wobj to wobj_plate, Building Plate
    done = abb.send_and_wait(rrc.SetWorkObject('wobj_plate'))

    speed_move = 100
    speed_pick_and_place = 20
    speed_safe_positions = 200
    for position in place_positions:
        # pick shingle
        instruction = 'r_WS_OpenVacuumGripper'
        done = abb.send_and_wait(rrc.CustomInstruction(instruction, string_values, float_values))
        # 1. move to safety
        done = abb.send_and_wait(rrc.MoveToJoints(pick_safety_joints, external_axes, speed_safe_positions, rrc.Zone.FINE))
        # 2. move above pick
        abb.send(rrc.MoveToFrame(pick_approach, speed_move, rrc.Zone.Z10, rrc.Motion.JOINT))
        # 3. move to pick
        abb.send(rrc.MoveToFrame(pick_position, speed_pick_and_place, rrc.Zone.FINE, rrc.Motion.LINEAR))
        # 4. pick shingle
        instruction = 'r_WS_CloseVacuumGripper'
        done = abb.send_and_wait(rrc.CustomInstruction(instruction, string_values, float_values))
        # 5. move back to above pick
        abb.send(rrc.MoveToFrame(pick_position, speed_pick_and_place, rrc.Zone.Z10, rrc.Motion.LINEAR))
        # 6. move back to safety
        done = abb.send_and_wait(rrc.MoveToJoints(pick_safety_joints, external_axes, speed_safe_positions, rrc.Zone.FINE))

        # place shingle
        offset_value = 100
        # 1. move above place position
        position.point[2] += offset_value
        abb.send(rrc.MoveToFrame(position, speed_move, rrc.Zone.Z10, rrc.Motion.JOINT))
        # 2. move to place position
        position.point[2] -= offset_value
        abb.send(rrc.MoveToFrame(position, speed_pick_and_place, rrc.Zone.FINE, rrc.Motion.LINEAR))
        # 3. place shingle
        instruction = 'r_WS_OpenVacuumGripper'
        done = abb.send_and_wait(rrc.CustomInstruction(instruction, string_values, float_values))
        # 4. move back above place position
        position.point[2] += offset_value
        abb.send(rrc.MoveToFrame(position, speed_pick_and_place, rrc.Zone.Z10, rrc.Motion.LINEAR))

    done = abb.send_and_wait(rrc.MoveToJoints(pick_safety_joints, external_axes, speed_safe_positions, rrc.Zone.FINE))

    # End of Code
    print('Finished')

    # Close client
    ros.close()
    ros.terminate()
