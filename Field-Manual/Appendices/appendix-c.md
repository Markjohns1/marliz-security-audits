# Appendix C: Marliz Remediation Checklist

---

**Server Hardening**
- [ ] SSH Root Login Disabled
- [ ] SSH Password Auth Disabled (Key Only)
- [ ] Fail2Ban Installed and Configured
- [ ] UFW/Iptables Firewall Active (Allow 80, 443, 22 only)

**Application Security**
- [ ] `.env` file is in `.gitignore`
- [ ] All `include()` calls use whitelisting
- [ ] Session cookies are `HttpOnly` and `Secure`
- [ ] Error Reporting is `Off` in production
- [ ] File Uploads are sanitized and renamed

**Database Security**
- [ ] Remote Root Login Disabled
- [ ] Database user has limited privileges (Revert `GRANT ALL`)
- [ ] Backups are automated and encrypted

**Process**
- [ ] Developers have read the Marliz Field Manual Part 1
- [ ] Incident Response Plan is printed and on the desk
