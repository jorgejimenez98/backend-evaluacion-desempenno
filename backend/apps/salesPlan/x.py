lista = [('Comestibles', 'Loby Bar', 1, 305.2),
         ('Comestibles', 'Loby Bar', 5, 87.23),
         ('Comestibles', 'Piano Bar', 2, 236.9),
         ('Comestibles', 'Piano Bar', 8, 412.69),
         ('Bebidas', 'Loby Bar', 3, 145.37),
         ('Bebidas', 'Loby Bar', 5, 640.81),
         ('Bebidas', 'Piano Bar', 12, 94.51),
         ('Tabacos', 'Cafeteria', 4, 498.12),
         ('Tabacos', 'Cafeteria', 6, 651.3),
         ('Tabacos', 'Piano Bar', 8, 813.5),
         ('Tabacos', 'Piano Bar', 11, 843.25),
         ('Otros', 'Loby Bar', 6, 140.24),
         ('Otros', 'Piano Bar', 9, 267.06),
         ('Otros', 'Cafeteria', 12, 695.12)]

if len(lista) > 0:
    data = []
    cur_fami = lista[0][0]
    cur_pvta = lista[0][1]
    pvtas = []
    meses = ['', '', '', '', '', '', '', '', '', '', '', '', 0]
    tot_fami = [0] * 13
    tot = [0] * 13

    for pvfa in lista:
        if pvfa[1] != cur_pvta:
            pvtas.append((cur_pvta, meses[:]))
            cur_pvta = pvfa[1]
            meses = ['', '', '', '', '', '', '', '', '', '', '', '', 0]
        if pvfa[0] != cur_fami:
            data.append((cur_fami, pvtas[:], tot_fami[:]))
            cur_fami = pvfa[0]
            pvtas = []
            tot_fami = [0] * 13
        meses[pvfa[2] - 1] = pvfa[3]
        meses[12] += pvfa[3]
        tot_fami[pvfa[2] - 1] += pvfa[3]
        tot_fami[12] += pvfa[3]
        tot[pvfa[2] - 1] += pvfa[3]
        tot[12] += pvfa[3]

    pvtas.append((cur_pvta, meses[:]))
    data.append((cur_fami, pvtas[:], tot_fami[:]))
    data.append(tot)

    print(data)

x = [('Comestibles', [('Loby Bar', [305.2, '', '', '', 87.23, '', '', '', '', '', '', '', 392.43]),
                      ('Piano Bar', ['', 236.9, '', '', '', '', '', 412.69, '', '', '', '', 649.59])],
      [305.2, 236.9, 0, 0, 87.23, 0, 0, 412.69, 0, 0, 0, 0, 1042.02]),
     ('Bebidas', [('Loby Bar', ['', '', 145.37, '', 640.81, '', '', '', '', '', '', '', 786.18]),
                  ('Piano Bar', ['', '', '', '', '', '', '', '', '', '', '', 94.51, 94.51])],
      [0, 0, 145.37, 0, 640.81, 0, 0, 0, 0, 0, 0, 94.51, 880.6899999999999]),
     ('Tabacos', [('Cafeteria', ['', '', '', 498.12, '', 651.3, '', '', '', '', '', '', 1149.42]),
                  ('Piano Bar', ['', '', '', '', '', '', '', 813.5, '', '', 843.25, '', 1656.75])],
      [0, 0, 0, 498.12, 0, 651.3, 0, 813.5, 0, 0, 843.25, 0, 2806.17]),
     ('Otros', [('Loby Bar', ['', '', '', '', '', 140.24, '', '', '', '', '', '', 140.24]),
                ('Piano Bar', ['', '', '', '', '', '', '', '', 267.06, '', '', '', 267.06]),
                ('Cafeteria', ['', '', '', '', '', '', '', '', '', '', '', 695.12, 695.12])],
      [0, 0, 0, 0, 0, 140.24, 0, 0, 267.06, 0, 0, 695.12, 1102.42]),
     [305.2, 236.9, 145.37, 498.12, 728.04, 791.54, 0, 1226.19, 267.06, 0, 843.25, 789.63, 5831.3]]
