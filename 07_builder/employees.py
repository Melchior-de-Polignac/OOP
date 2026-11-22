from dataclasses import dataclass
from datetime import date


@dataclass
class Employee:
    first_name: str
    last_name: str
    email: str
    department: str
    position: str
    salary: float
    start_date: str
    manager_id: int | None = None
    phone: str | None = None
    address: str | None = None
    emergency_contact: str | None = None
    office_location: str | None = None
    contract_type: str = "permanent"
    has_parking: bool = False
    has_laptop: bool = False
    has_vpn_access: bool = False
    has_admin_rights: bool = False


class EmployeeBuilder:
    def __init__(self):
        self._fields = {}

    def with_name(self, first_name, last_name):
        self._fields["first_name"] = first_name
        self._fields["last_name"] = last_name
        return self

    def with_email(self, email):
        self._fields["email"] = email
        return self

    def with_job(self, department, position, salary):
        self._fields["department"] = department
        self._fields["position"] = position
        self._fields["salary"] = salary
        return self

    def with_start_date(self, start_date):
        self._fields["start_date"] = start_date
        return self

    def with_manager(self, manager_id):
        self._fields["manager_id"] = manager_id
        return self

    def with_contact(self, phone=None, address=None, emergency_contact=None):
        self._fields["phone"] = phone
        self._fields["address"] = address
        self._fields["emergency_contact"] = emergency_contact
        return self

    def with_office(self, office_location, contract_type="permanent"):
        self._fields["office_location"] = office_location
        self._fields["contract_type"] = contract_type
        return self

    def with_equipment(self, laptop=False, parking=False):
        self._fields["has_laptop"] = laptop
        self._fields["has_parking"] = parking
        return self

    def with_access(self, vpn=False, admin=False):
        self._fields["has_vpn_access"] = vpn
        self._fields["has_admin_rights"] = admin
        return self

    def build(self):
        required = [
            "first_name",
            "last_name",
            "email",
            "department",
            "position",
            "salary",
            "start_date",
        ]
        missing = [name for name in required if name not in self._fields]
        if missing:
            raise ValueError(f"missing required fields: {', '.join(missing)}")
        if not self._fields["first_name"] or not self._fields["last_name"]:
            raise ValueError("name is required")
        if "@" not in self._fields["email"]:
            raise ValueError("valid email is required")
        if self._fields["salary"] < 0:
            raise ValueError("salary cannot be negative")
        return Employee(**self._fields)


class DeveloperBuilder(EmployeeBuilder):
    def __init__(self, first_name, last_name, email):
        super().__init__()
        self.with_name(first_name, last_name)
        self.with_email(email)
        self.with_job("Engineering", "Senior Developer", 75000)
        self.with_start_date(date.today().isoformat())
        self.with_equipment(laptop=True)
        self.with_access(vpn=True, admin=True)


if __name__ == "__main__":
    intern = (
        EmployeeBuilder()
        .with_name("Jane", "Smith")
        .with_email("jane.smith@company.com")
        .with_job("Marketing", "Intern", 15000)
        .with_start_date("2024-02-01")
        .with_office("Paris", contract_type="internship")
        .with_equipment(laptop=True)
        .build()
    )
    print(intern)

    print(DeveloperBuilder("John", "Doe", "john@company.com").build())

    try:
        EmployeeBuilder().with_name("Bob", "Lee").build()
    except ValueError as error:
        print(error)
