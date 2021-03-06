import os

def test(parameters, user, job):
  outfile = open(os.path.dirname(os.path.dirname(__file__)) + '/data/' + user + '/' + str(job) +'/inputMD', 'w')
  outfile.write("sim_type = " + parameters['sim_type'] + "\n")
  outfile.write("backend = " + parameters['backend'] + "\n")
  outfile.write("backend_precision = " + parameters['backend_precision'] + "\n")
  outfile.write("interaction_type = " + parameters['interaction_type'] + "\n")
  outfile.write("\n")
  outfile.write("steps = " + str(parameters['steps']) + "\n")
  outfile.write("newtonian_steps = " + str(parameters['newtonian_steps']) + "\n")
  outfile.write("diff_coeff = " + str(parameters['diff_coeff']) + "\n")
  outfile.write("thermostat = " + parameters['thermostat'] + "\n")
  outfile.write("\n")
  outfile.write("salt_concentration = " + str(parameters['salt_concentration']) + "\n")
  outfile.write("base_angle_range = " + str(parameters['base_angle_range']) + "\n")
  outfile.write("strand_orthogonality_range = " + str(parameters['strand_orthogonality_range']) + "\n")
  outfile.write("\n")
  outfile.write("T = " + parameters['t'] + "\n")
  outfile.write("dt = " + str(parameters['dt']) + "\n")
  outfile.write("verlet_skin = " + str(parameters['verlet_skin']) + "\n")
  outfile.write("\n")
  outfile.write("topology = " + parameters['topology'] + "\n")
  outfile.write("conf_file = " + parameters['conf_file'] + "\n")
  outfile.write("last_conf_file = " + parameters['last_conf_file'] + "\n")
  outfile.write("trajectory_file = " + parameters['trajectory_file'] + "\n")
  outfile.write("refresh_vel = " + str(parameters['refresh_vel']) + "\n")
  outfile.write("log_file = " + parameters['log_file'] + "\n")
  outfile.write("restart_step_counter = " + str(parameters['restart_step_counter']) + "\n")
  outfile.write("energy_file = " + parameters['energy_file'] + "\n")
  outfile.write("print_conf_interval = " + str(parameters['print_conf_interval']) + "\n")
  outfile.write("print_energy_every = " + str(parameters['print_energy_every']) + "\n")
  outfile.write("time_scale = " + parameters['time_scale'] + "\n")
  outfile.close();
  return 0

def get_progess(user, job):
  traj = open(os.path.dirname(os.path.dirname(__file__)) + '/data/' + user + '/' + str(job) +'/trajectory.dat', 'r')
  progress = 0
  line = traj.readline()
  while (line):
    temp = line.split()
    if temp[0] == 't':
      progress = temp[2]
    line = traj.readline()
  
  print "debug: " + progress
  
  return 0
