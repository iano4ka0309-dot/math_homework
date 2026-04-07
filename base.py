from itertools import product

def check_access(
        is_employee,
          is_verified, 
          is_premium, 
          is_admin,
          is_banned
          ):
    base = is_employee and is_verified and not is_banned
    premium = (is_employee or is_premium) and is_verified and not is_banned
    admin = is_admin and is_verified and not is_banned
    secret = (is_admin or (is_employee and is_premium)) and is_verified and not is_banned
    return {
        "base": base,
        "premium": premium,
        "admin": admin,
        "secret": secret
    }

print (f"{'Emp':<6}{'Ver':<6}{'Prem':<6}{'Adm':<6}{'Ban':<6}|{'Base':<6}{'Prem':<6}{'Adm':<6}{'Secr':<6}")
print("-" * 65)

for combination in product([True, False], repeat=5):
    is_employee, is_verified, is_premium, is_admin, is_banned = combination
    result = check_access(is_employee, is_verified, is_premium, is_admin, is_banned)
    print(f"{int(is_employee):<6}{int(is_verified):<6}{int(is_premium):<6}{int(is_admin):<6}{int(is_banned):<6}| {int(result['base']):<6}{int(result['premium']):<6}{int(result['admin']):<6}{int(result['secret']):<6}")

count = 0
full_access_cases = []

for combination in product([True, False], repeat=5):
    is_employee, is_verified, is_premium, is_admin, is_banned = combination
    result = check_access(is_employee, is_verified, is_premium, is_admin, is_banned)
    if result['base'] and result['premium'] and result['admin'] and result['secret']:
        count += 1
        full_access_cases.append(f"Emp={int(is_employee)} Ver={int(is_verified)} Prem={int(is_premium)} Adm={int(is_admin)} Ban={int(is_banned)}")
print(f"Повний доступ: {count} випадків:")
for item in full_access_cases:
    print(item)


count = 0
premium_without_base_cases = []
for combination in product([True, False], repeat=5):
    is_employee, is_verified, is_premium, is_admin, is_banned = combination
    result = check_access(is_employee, is_verified, is_premium, is_admin, is_banned)
    if  not result['base'] and result['premium']:
        count += 1
        premium_without_base_cases.append(f"Emp={int(is_employee)} Ver={int(is_verified)} Prem={int(is_premium)} Adm={int(is_admin)} Ban={int(is_banned)}")
#Людина не є співробітником, але має преміум підписку — тому Base недоступний, але Premium є!
print(f"Преміум без базового: {count} випадків:")
for item in premium_without_base_cases:
    print(item)

       
