# Security Policy

## Supported Versions

We support the following versions of this project:

| Version | Supported          |
| ------- | ------------------ |
| 0.0.4   | :white_check_mark: |
| 0.0.3   | :white_check_mark: |
| 0.0.2   | :white_check_mark: |
| 0.0.1   | :x:                |

## Reporting a Vulnerability

If you discover a security vulnerability in this project, please report it responsibly:

### How to Report

1. **Do NOT open a public issue** for security vulnerabilities
2. Send an email to: zenjiro0123@gmail.com
3. Include the following information:
   - Description of the vulnerability
   - Steps to reproduce the issue
   - Potential impact
   - Suggested fix (if you have one)

### What to Expect

- **Acknowledgment**: We will acknowledge receipt of your report within 48 hours
- **Investigation**: We will investigate the issue and determine its severity
- **Updates**: We will provide regular updates on our progress
- **Resolution**: We will work to resolve the issue as quickly as possible
- **Credit**: We will credit you for the discovery (unless you prefer to remain anonymous)

### Response Timeline

- **Critical vulnerabilities**: 24-48 hours
- **High severity**: 1 week
- **Medium/Low severity**: 2-4 weeks

## Security Best Practices

When using this package:

1. **Keep dependencies updated**: Regularly update to the latest version
2. **Review code**: This is an open-source project - review the code before use
3. **Validate inputs**: Always validate inputs to the `add_one` function
4. **Use in trusted environments**: This is a demonstration package

## Scope

This security policy applies to:
- The main package code in `src/package_trial_zenjiro/`
- Build and distribution processes
- Documentation and examples

## Out of Scope

The following are considered out of scope:
- Issues in dependencies (report to respective maintainers)
- General Python security issues
- Issues in development tools or test code

## Security Considerations

### Current Security Status

This package:
- Contains minimal code surface area (single function)
- Has no external dependencies in runtime
- Uses standard Python operations only
- Has been thoroughly tested

### Potential Risks

While this is a simple demonstration package, be aware of:
- **Input validation**: The `add_one` function accepts any numeric input
- **Type errors**: Invalid inputs will raise TypeError
- **Numerical overflow**: Very large numbers may cause issues

### Recommendations

For production use:
1. Validate inputs before calling `add_one`
2. Handle potential TypeErrors appropriately
3. Consider numerical limits for your use case
4. Test thoroughly in your environment

## Contact

For security-related questions or concerns:
- Email: zenjiro0123@gmail.com
- Subject: [SECURITY] Package Trial Zenjiro

Thank you for helping keep this project secure! 🔒