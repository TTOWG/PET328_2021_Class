def calculate_cumulative_oil_production(nx, ny, nz, N, Boi, Bob, ce, co, Pb, Pi_values, Pnow_values):
    total_np = 0
    block_np_list = []

    for k in range(nz):
        Pi = Pi_values[k]
        for j in range(ny):
            for i in range(nx):
                block_n_order = k * ny * nx + j * nx + i + 1
                Pnow = Pnow_values[block_n_order - 1]
                bo = Bob * (1 - co * (Pnow - Pb))
                block_np = (N * Boi * ce * (Pi - Pnow)) / bo
                total_np += block_np
                block_np_list.append(block_np)

    return total_np, block_np_list
