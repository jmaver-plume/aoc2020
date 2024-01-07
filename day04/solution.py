import re


def parse():
    with open('input') as f:
        data = f.read()
    raw_passports = data.split('\n\n')

    def parse_raw_transport(raw_transport):
        pairs = [pair.split(':') for pair in raw_transport.replace('\n', ' ').split(' ')]
        return {key: value for key, value in pairs}

    return [parse_raw_transport(transport) for transport in raw_passports]


def is_valid_passport_p1(passport):
    return ('byr' in passport and
            'iyr' in passport and
            'eyr' in passport and
            'hgt' in passport and
            'hcl' in passport and
            'ecl' in passport and
            'pid' in passport)


def is_valid_passport_p2(passport):
    if not is_valid_passport_p1(passport):
        return False

    byr = int(passport['byr'])
    if not (1920 <= byr <= 2002):
        return False

    iyr = int(passport['iyr'])
    if not (2010 <= iyr <= 2020):
        return False

    eyr = int(passport['eyr'])
    if not (2020 <= eyr <= 2030):
        return False

    hgt = passport['hgt']
    match = re.match(r"(\d+)(in|cm)", hgt)
    if not match:
        return False
    if match.group(2) == 'cm' and not (150 <= int(match.group(1)) <= 193):
        return False
    if match.group(2) == 'in' and not (59 <= int(match.group(1)) <= 76):
        return False

    hcl = passport['hcl']
    if not bool(re.fullmatch(r"#[0-9a-f]{6}", hcl)):
        return False

    ecl = passport['ecl']
    if ecl not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
        return False

    pid = passport['pid']
    if not bool(re.fullmatch(r"[0-9]{9}", pid)):
        return False

    return True


def p1():
    passports = parse()
    valid_passports = [passport for passport in passports if is_valid_passport_p1(passport)]
    return len(valid_passports)


def p2():
    passports = parse()
    valid_passports = [passport for passport in passports if is_valid_passport_p2(passport)]
    return len(valid_passports)


def main():
    print(f'p2: {p1()}')
    print(f'p2: {p2()}')


main()
