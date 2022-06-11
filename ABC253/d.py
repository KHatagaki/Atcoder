
def main():
    n,a,b = map(int,input().split())
    sum = n * (n + 1) // 2
    if(a % b != 0 and b % a != 0):
        syou_a = n // a
        syou_b = n // b
        d = int(lcm_e(a,b))
        syou_d = n // d
        d_sum = (d + syou_d * d) * syou_d // 2
        a_sum = (a + syou_a * a) * syou_a // 2
        b_sum = (b + syou_b * b) * syou_b // 2
        sum = sum - a_sum - b_sum + d_sum
    else:
        if(a >= b):
            syou_b = n // b
            b_sum = (b + syou_b * b) * syou_b // 2
            sum -= b_sum
        else:
            syou_a = n // a
            a_sum = (a + syou_a * a) * syou_a // 2
            sum -= a_sum
    return sum

def gcd_e(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm_e(a, b):
        return a * b / gcd_e(a, b)

if __name__ == "__main__":
    print(int(main()))