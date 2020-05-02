def parse_Gaussian_file(file_in):
    ener = []
    osc = []
    with open(file_in, 'r') as file_object:
        for line in file_object:
            if 'Excited State' in line:
                row = line.split()
                ener.append(float(row[6]))
                osc.append(float(row[8].replace('f=','')))
    return ener, osc

def parse_Dalton_file(file):
    ROOTS= None
    energies = []
    deltas = []
    sigmas = []
    with open(file, 'r') as file_object:
        out_output = file_object.readlines()
        for i, line in enumerate(out_output):
            if ".ROOTS" in line:
                ROOTS=int(out_output[i+1])
            elif 'Two-photon absorption summary ' in line:
                for l in range(i, i+5+(ROOTS*2)):
                    if 'Linear' in out_output[l]:
                        energy=float(out_output[l].split()[2])
                        D=float(out_output[l].split()[6])
                        sigma=float(out_output[l].split()[7])
                        energies.append(energy)
                        deltas.append(D)
                        sigmas.append(sigma)
    return energies, deltas, sigmas
