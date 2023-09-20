use color_eyre::Result;

pub fn setup_debug_tools() -> Result<()> {
    // only excecute this loop once
    if std::env::var("RUST_BACKTRACE").is_ok()
        && (std::env::var("RUST_BACKTRACE")? == "1" || std::env::var("RUST_BACKTRACE")? == "full")
    {
        return Ok(());
    }

    // setup color_eyre
    std::env::set_var("RUST_BACKTRACE", "1");
    color_eyre::install()?;

    Ok(())
}

/// # Examples
///
/// ```
/// use quocca::dump;
/// let address = 2;
/// let value = 3;
/// dump!("address = {}  value = 0b{:08b}", address, value);
/// ```
#[macro_export]
macro_rules! dump {
    () => {
        eprintln!("[{}:{}]", file!(), line!());
    };
    ($($arg:tt)*) => {
        eprintln!("[{}:{}] {}", file!(), line!(), format!($($arg)*));
    };
    ($($val:expr),+$(,)?) => {
        ($($crate::dump!($val)),+,)
    };
}

/// # Examples
///
/// ```
/// use quocca::dmp;
/// let address = 2;
/// let value = 3;
/// dmp!(address, value);
/// ```
#[macro_export]
macro_rules! dmp {
    ($($a:expr),*) => {
		eprintln!(concat!("[", file!(), ":", line!(), "] ", $(stringify!($a), " = {:?}  "),*), $($a),*);
	}
}
