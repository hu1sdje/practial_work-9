for s in range(1, 10):
    for e in range(10):
        for n in range(10):
            for d in range(10):
                for m in range(1, 10):
                    for o in range(10):
                        for y in range(10):
                            for r in range(10):
                                send = s * 1000 + e * 100 + n * 10 + d
                                more = m * 1000 + o * 100 + r * 10 + e
                                money = m * 10000 + o * 1000 + n * 100 + e * 10 + y
                                if send + more == money:
                                    print(f'{send} + {more} = {money}')