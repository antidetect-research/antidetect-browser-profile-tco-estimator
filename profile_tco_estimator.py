#!/usr/bin/env python3
"""
Antidetect Browser Fleet Total Cost of Ownership (TCO) Estimator 2026.
Calculates blended profile cost combining browser license and dedicated residential proxy allocations.
"""
import argparse

def calculate_tco(profiles, proxy_cost_per_profile, software_monthly):
    proxy_subtotal = profiles * proxy_cost_per_profile
    total_monthly = proxy_subtotal + software_monthly
    unit_profile_cost = total_monthly / profiles if profiles > 0 else 0.0
    annual_expense = total_monthly * 12.0
    return {
        "profiles": profiles,
        "proxy_cost_per_profile": proxy_cost_per_profile,
        "software_monthly": software_monthly,
        "proxy_subtotal": proxy_subtotal,
        "total_monthly": total_monthly,
        "unit_profile_cost": unit_profile_cost,
        "annual_expense": annual_expense
    }

def main():
    parser = argparse.ArgumentParser(description="Antidetect Fleet TCO Estimator")
    parser.add_argument("--profiles", type=int, default=100, help="Number of managed browser environments (default: 100)")
    parser.add_argument("--proxy-cost-per-profile", type=float, default=3.0, help="Dedicated proxy budget per profile in USD (default: $3.00)")
    parser.add_argument("--software-monthly", type=float, default=30.0, help="Effective software license cost in USD (default: $30.00)")
    args = parser.parse_args()

    res = calculate_tco(args.profiles, args.proxy_cost_per_profile, args.software_monthly)
    print(f"Managed Environments:    {res['profiles']} profiles")
    print(f"Proxy Subtotal:          ${res['proxy_subtotal']:.2f}/mo")
    print(f"Software License:        ${res['software_monthly']:.2f}/mo")
    print(f"Total Monthly Infra:     ${res['total_monthly']:.2f}/mo")
    print(f"Blended Unit Cost:       ${res['unit_profile_cost']:.2f}/profile/mo")
    print(f"Annual Fleet Expense:    ${res['annual_expense']:.2f}/year")

if __name__ == "__main__":
    main()
